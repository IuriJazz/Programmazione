from hexalattice.hexalattice import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#  creazione di una griglia monocolore
hex_centers, h_ax = create_hex_grid(nx=31, ny=31, do_plot=True, min_diam=1,
                                    face_color=[0., 0., 0., 0.],
                                    edge_color=[0., 0., 0., 0.])

create_hex_grid(nx=31, ny=31, do_plot=True, face_color=[0., 0., 0., 0.],  # colore interno
                edge_color=[0., 0., 0., 0.],  # colore bordo
                h_ax=h_ax, plotting_gap=0.25, min_diam=1)


# tutto quello che c'è di seguito serve per i colori
create_hex_grid(nx=31, ny=31, do_plot=True, h_ax=h_ax)

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]

#  fai uncomment per scegliere quale tipologia di mappa mostrare
colors = np.random.uniform(0., 1., (961, 4))  # colora tutte le celle di colori casuali
colors_face = np.ones([961, 4])  # colora tutte le celle di bianco RGBA(1, 1, 1, 1), interessante
#  colors = np.zeros([961, 4]) # colora tutte le celle di nulla RGBA(0, 0, 0, 0), A = trasparenza

colors[480] = [0, 1, 0, 1]  # serve per selezionare e colorare una determinata cella
colors[481] = [0, 1, 0, 0]

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,
                                  face_color=colors_face, edge_color=colors,
                                  min_diam=1., plotting_gap=0.15,
                                  rotate_deg=0, h_ax=h_ax, line_width=2.5)
# fino a qui riguarda i colori

# questi sono i limiti di numeri da mostrare tramite la libreria matplotlib
h_ax.set_xlim(-16.5, 16.)
h_ax.set_ylim(-14, 14)


#  impostazione di ogni quanto ci sarà un tick
loc = ticker.MultipleLocator(base=4.33)
# this locator puts ticks at regular intervals 0.866(distanza di ogni cella in verticale)
h_ax.yaxis.set_major_locator(loc)
# qui è stata impostata una distanza di 5 esagoni per ogni tick, la distanza in verticale
# di ogni esagono è di 0.866, 0.866 * 5 = 4.33 == un tick ogni 5 esagoni


#  impostazione dei nomi dei tick
num = [-20, -15, -10, -5, 0, 5, 10, 15]
h_ax.set_yticklabels(num)
#  qui si cambiano i nomi dei Ticks = i numeri delle assi x/y

#  mostra i tick (griglia)
plt.grid()



# lista di zero, come esempio di lista giocatori
pg = np.random.uniform(0., 1., (50, 1))

plt.legend(([pg]), title='Top Possedimenti:', bbox_to_anchor=(0.996, 1.0084),
           loc='upper left', title_fontsize=13, prop={'size': 11},
           handlelength=0, handletextpad=0, markerfirst=0)

plt.title('Terreni dei giocatori')


#  impostazione della dimensione esatta dell'immagine
figure = plt.gcf()  # get current figure
figure.set_size_inches(14.1, 10)


#  salva l'immagine come png con un determinato dpi (qualità d'immagine)
plt.savefig('Territori.png', dpi=500)

plt.close()
