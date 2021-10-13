import numpy as np
import qepy

try:
    from mpi4py import MPI
except Exception:
    comm = None
else:
    comm = MPI.COMM_WORLD
    comm = comm.py2f()

fname = 'qe_in.in'

qepy.qepy_pwscf(fname, comm)

embed = qepy.qepy_common.embed_base()

qepy.qepy_electrons_scf(0, 0, embed)

nscf = qepy.control_flags.get_n_scf_steps()
conv_flag = bool(qepy.control_flags.get_conv_elec())
info = 'Converged {} at {} steps'.format(conv_flag, nscf)
qepy.qepy_mod.qepy_write_stdout(info)

qepy.qepy_calc_energies(embed)
etotal = embed.etotal

qepy.qepy_forces(0)
forces = qepy.force_mod.get_array_force().T

stress = np.ones((3, 3), order='F')
qepy.stress(stress)

qepy.punch('all')
qepy.qepy_stop_run(0, what = 'no')
