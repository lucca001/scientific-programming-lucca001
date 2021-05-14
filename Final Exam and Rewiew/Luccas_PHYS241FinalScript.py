import mathcal as mathcal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mathtext

from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from convert_units import convert_units
from parse_file_name import parse_file_name
from annotate_graph import annotate_graph

display_graph = True
data = two_column_text_read("Cu.Fm-3m.GGA-PBE.volumes_energies.dat")
quadratic = quadratic_fit(data)
statistics = bivariate_statistics(data)
eos_fit, fit_parameters = fit_eos(data[0, :], data[1, :], quadratic, "birch-murnaghan")
Volumes = (convert_units(data[0, :], "cubic bohr", "cubic angstrom"))
Energies = (convert_units(data[1, :], "rydberg", "ev"))
bulk_modulus = convert_units(fit_parameters[1], "rydberg per cubic bohr", "gigapascals")
fit_x_values = data[0, :]
fit_data = fit_curve_array(quadratic, fit_x_values[0], fit_x_values[-1])

print(fit_data)

plt.plot(
    convert_units(fit_data[0, :], "cubic bohr", "cubic angstrom"),
    convert_units(fit_data[1, :], "rydberg", "ev"),
    color="black"
)
plt.plot(Volumes, Energies, "o", color="blue")
plt.xlabel(r'$\mathcal{V}$'+" "+"(eV/atom)")
plt.ylabel(r'$\mathcal{E}$'+" "+r"($\AA^{3}$/atom)")
annotate_graph(parse_file_name("Cu.Fm-3m.GGA-PBE.volumes_energies.dat"))

if display_graph == True:
    plt.show()
else:
    plt.savefig()
