#!/usr/bin/env python3
import qepy

try:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
except Exception:
    comm = None

from qepy.calculator import QEpyCalculator
import ase.io
from ase.io.trajectory import Trajectory
from ase import units
from ase.md.andersen import Andersen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

inputfile = 'qe_in.in'

calc = QEpyCalculator(comm = comm, inputfile = inputfile)

atoms = ase.io.read(inputfile, format='espresso-in')

atoms.set_calculator(calc)

T = 340
MaxwellBoltzmannDistribution(atoms, temperature_K = T, force_temp=True)

dyn = Andersen(atoms, 1.5 * units.fs, temperature_K = T, andersen_prob=0.02)

step = 0
interval = 1

def printenergy(a=atoms):
    global step, interval
    epot = a.get_potential_energy() / len(a)
    ekin = a.get_kinetic_energy() / len(a)
    if a.calc.rank == 0 :
        print("Step={:<8d} Epot={:.5f} Ekin={:.5f} T={:.3f} Etot={:.5f}".format(
                step, epot, ekin, ekin / (1.5 * units.kB), epot + ekin), flush = True)
    step += interval


dyn.attach(printenergy, interval=1)

traj = Trajectory("md.traj", "w", atoms)
dyn.attach(traj.write, interval=1)

dyn.run(5)
