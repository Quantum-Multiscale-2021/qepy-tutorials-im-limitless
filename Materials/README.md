# QEpy-Tutorials

This folder contains
 - examples-scf
 - jupyter-scf
 - jupyter-nvt

### `examples-scf` Python scripts
The folder contains 4 examples. The most important of them is `test_pwscf.py` which deals with a simple SCF. `test_pwscf_scf.py` is similar to `test_pwscf.py` except that it drives the SCF one cycle at a time.

`tmp2energy.py` are scripts to carry out one-shot evaluations of the energy (no SCF)  given a wavefunction folder. `tmp2energy_pw.py` does the same, but is also able to use any exchange-correlation functional available in QE.

### `jupyter-scf` Jupyter Notebooks
Contains a jupyter notebook version of `test_pwscf_scf.py`.


### `jupyter-nve` Jupyter Notebooks
Contains a jupyter notebook to run NVE AIMD with ASE and QEpy as "calculator".
