# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from hexalattice.hexalattice import *

#hex_centers, _ = create_hex_grid(nx=5,
#                                 ny=5,
#                                 do_plot=True)
#plt.show()

_, h_ax = create_hex_grid(nx=10,
                          ny=10,
                          rotate_deg=0,
                          n=0,
                          do_plot=True,
                          edge_color=(0.85, 0.85, 0.85)
                          )

create_hex_grid(nx=10,
                ny=10,
                rotate_deg=0,
                do_plot=True,
                edge_color=(0.25, 0.25, 0.25),
                h_ax=h_ax,
                plotting_gap=0.3
                )
plt.show()
