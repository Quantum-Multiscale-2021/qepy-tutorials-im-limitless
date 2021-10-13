import numpy as np
import qepy

try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    comm = comm.py2f()
except Exception:
    comm = None

fname = 'qe_in.in'

qepy.qepy_pwscf(fname, comm)

embed = qepy.qepy_common.embed_base()

qepy.control_flags.set_niter(1)
for i in range(60):
    if i>0 : embed.initial = False
    embed.mix_coef = -1.0
    qepy.qepy_electrons_scf(0, 0, embed)
    embed.mix_coef = 0.7
    qepy.qepy_electrons_scf(0, 0, embed)
    if qepy.control_flags.get_conv_elec() : break

qepy.qepy_calc_energies(embed)
etotal = embed.etotal

qepy.qepy_forces(0)
forces = qepy.force_mod.get_array_force().T

stress = np.ones((3, 3), order='F')
qepy.stress(stress)

qepy.punch('all')
qepy.qepy_stop_run(0, what = 'no')
