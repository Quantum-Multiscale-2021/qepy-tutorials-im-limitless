import qepy
try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    comm = comm.py2f()
except Exception:
    comm = None

oldxml = False # oldxml version QE

fname = 'qe_in.in'
qepy.qepy_pwscf(fname, comm, oldxml)

embed = qepy.qepy_common.embed_base()

if oldxml :
    qepy.oldxml_pw_restart.pw_readfile('header')
    qepy.oldxml_pw_restart.pw_readfile('reset')
    qepy.oldxml_pw_restart.pw_readfile('dim')
    qepy.oldxml_pw_restart.pw_readfile('bs')
    if qepy.basis.get_starting_pot().strip() != 'file' :
        qepy.oldxml_potinit(starting = 'file')
    if qepy.basis.get_starting_wfc().strip() != 'file' :
        qepy.oldxml_wfcinit(starting = 'file')
else :
    qepy.qepy_pw_restart_new.qepy_read_xml_file(alloc=False)
    if qepy.basis.get_starting_pot().strip() != 'file' :
        qepy.qepy_potinit(starting = 'file')
    if qepy.basis.get_starting_wfc().strip() != 'file' :
        qepy.qepy_wfcinit(starting = 'file')

energy = qepy.qepy_calc_energies(embed)
qepy.qepy_stop_run(0, what = 'no')
