import qepy
try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    comm = comm.py2f()
except Exception:
    comm = None

oldxml = False # oldxml version QE

inputobj = qepy.qepy_common.input_base()
#-----------------------------------------------------------------------
inputobj.prefix = 'al'
# inputobj.tmp_dir = './al.wfx/'
#-----------------------------------------------------------------------
if comm : inputobj.my_world_comm = comm
qepy.qepy_initial(inputobj)

if oldxml :
    qepy.oldxml_read_file()
else :
    qepy.read_file()

embed = qepy.qepy_common.embed_base()
energy = qepy.qepy_calc_energies(embed)
qepy.qepy_stop_run(0, what = 'no')
# Newer version QE (>6.3) (XML file name is 'data-file-schema.xml')
# Olderversion QE (XML file name is 'data-file.xml')
