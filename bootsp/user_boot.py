# This software is distributed under the 3-clause BSD License.
# archive version create 25 Jan 2023
# A driver for boot_sp for command-line users

import sys
import numpy as np
import mpisppy.utils.config as config
import mpisppy.confidence_intervals.ciutils as ciutils
import bootsp.boot_utils as boot_utils
import bootsp.boot_sp as boot_sp

# TBD: we are using the mpi-sppy MPI wrapper to help windows users live without MPI.
import mpisppy.MPI as MPI
my_rank = MPI.COMM_WORLD.Get_rank()


def main_routine(cfg, module):
    """ The top level of user_boot; called by __main__
        and by drivers such as simulate_experiments.py
    Args:
        cfg (Config): paramaters
        module (Python module): contains the scenario creator function and helpers        
    Note:
        prints confidence interval results to the terminal
    """

    if cfg["xhat_fname"] is not None and cfg["xhat_fname"] != "None":
        xhat = ciutils.read_xhat(cfg["xhat_fname"])
    else:
        xhat = boot_utils.compute_xhat(cfg, module)
        
    if cfg.boot_method == "Extended":
        ci_optimal,ci_upper, ci_gap =  boot_sp.extended_bootstrap(cfg, module, xhat)
    elif cfg.boot_method == "Bagging_with_replacement":
        ci_optimal,ci_upper, ci_gap = boot_sp.bagging_bootstrap(cfg, module, xhat, replacement = True)
    elif cfg.boot_method == "Bagging_without_replacement":
        ci_optimal,ci_upper, ci_gap = boot_sp.bagging_bootstrap(cfg, module, xhat, replacement = False)
    elif cfg.boot_method == "Classical_quantile":
        ci_optimal,ci_upper, ci_gap =  boot_sp.classical_bootstrap(cfg, module, xhat, quantile = True)
    elif cfg.boot_method == "Classical_gaussian":
        ci_optimal,ci_upper, ci_gap =  boot_sp.classical_bootstrap(cfg, module, xhat, quantile = False)
    elif cfg.boot_method == "Subsampling":
        ci_optimal,ci_upper, ci_gap =  boot_sp.subsampling(cfg, module, xhat)
    else:
        raise ValueError(f"boot_method={cfg.boot_method} is not supported.")

    if my_rank == 0:
        # print result    
        print(f"ci for optimal function value: {ci_optimal}")
        print(f"ci for function value at xhat: {ci_upper}")
        print(f"ci for optimality gap: {ci_gap}")

if __name__ == '__main__':
    print("Archive version")
    if len(sys.argv) < 2:
        print("need module name")
        print("usage python boot_sp.py module --options")
        print("usage (e.g.): python -m boosp.user_boot farmer.json  --help")
        print("   note: module name should not end it .py")
        quit()

    module_name = sys.argv[1]
    cfg = boot_utils.cfg_from_parse(module_name, name="user_boot")
    boot_utils.check_BFs(cfg)

    module = boot_utils.module_name_to_module(cfg["module_name"])

    xhat_fname = cfg["xhat_fname"]

    main_routine(cfg, module)

