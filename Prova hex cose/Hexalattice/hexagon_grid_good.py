from hexalattice.hexalattice import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def coor(x=None, y=None, n=None):
    """
    Convertitore di coordinate da 0-960 | (-15, -15)-(15, 15) e viceversa.

    Se hai le assi X-Y ti basta scriverle separate da una virgola:
    x: int
    y: int
    n: None|DEFAULT
    (Es: coor(2, 3))

    Se hai il numero di cella, ti basta scrivere la n:
    n=int
    (Es: coor(n=240))
    """
    # qui trasformo le 960 celle in coordinate x=w, y=q
    coordinates = []
    for q in range(-15, 16):
        for w in range(-15, 16):
            coordinates.append((w, q))
    # ora coordinates ha una lista di coordinate da (-15, -15) a (15, 15)
    # con lo stesso principio posso scegliere facilmente anche la cella

    if n is None:
        return coordinates.index((x, y))  # ti trova il numero della cella
    elif x or y != int:
        return coordinates[n]  # ti trova la x e y
    else:
        print('Hai scritto qualcosa nella maniera scorretta, riprova per favore.')
    # ora se scrivi x e y, troverai la cella corrispondente, se scrivi la cella trovi la x-y
#  questa funzione la posso usare per trovare facilmente i numeri di cella


nero = [0., 0., 0., 1.]
trasparente = [0., 0., 0., 0.]
prato = [0.60784, 1., 0.60784, 1.]
nx = 31  # quantità di celle asse X
ny = 31  # quantità di celle asse Y

#  creazione di una griglia monocolore
hex_centers, h_ax = create_hex_grid(nx, ny, do_plot=True, min_diam=1,
                                    face_color=nero,
                                    edge_color=nero)

#  creazione griglia "bordino", con prato di base e bordi trasparenti
create_hex_grid(nx, ny, do_plot=True, face_color=prato,  # colore interno
                edge_color=trasparente,  # colore bordo
                h_ax=h_ax, plotting_gap=0.25, min_diam=1)

# tutto quello che c'è di seguito serve per i colori
create_hex_grid(nx, ny, do_plot=True, h_ax=h_ax)

x_hex_coords = hex_centers[:, 0]
y_hex_coords = hex_centers[:, 1]


#  TODO: da qui in poi, devi stare attento a come proseguire: devo avere in mente tutto con chiarezza

#  fai uncomment per scegliere quale tipologia di mappa mostrare
colors = np.random.uniform(0., 1., (961, 4))  # colora tutte le celle di colori casuali
#  colors = np.ones([961, 4])  # colora tutte le celle di bianco RGBA(1, 1, 1, 1), interessante
colors_face = np.zeros([961, 4])  # colora tutte le celle di nulla RGBA(0, 0, 0, 0), A = trasparenza

colors[480] = [1, 0, 0, 1]  # serve per selezionare e colorare una determinata cella
colors[481] = [1, 0, 0, 0]

# sono riuscito a creare una funzione che mi permette di convertire X-Y in numero e viceversa
colors[coor(15, -14)] = [0, 1, 0, 1]

plot_single_lattice_custom_colors(x_hex_coords, y_hex_coords,
                                  face_color=colors_face, edge_color=colors,
                                  min_diam=1., plotting_gap=0.15,
                                  rotate_deg=0, h_ax=h_ax, line_width=3.)
# fino a qui riguarda i colori

# TODO: pensa bene a come creare questa funzione
'''
per fare i combattimenti, dovrò fare un def che mi permetta di fare il combattimento tra due
celle. Quindi poter confrontare, ogni volta, quali sono le perdite dopo lo scontro.
Quindi qualcosa del tipo: se nella prima cella dopo lo scontro vince, il territorio passa
al conquistatore e viene tolto al conquistato.
'''


# questi sono i limiti di numeri da mostrare tramite la libreria matplotlib
h_ax.set_xlim(-16.5, 16.)
h_ax.set_ylim(-14, 14)

#  impostazione di ogni quanto ci sarà un tick
loc = ticker.MultipleLocator(base=4.33)
# questo locator mette i tick a un intervallo regolare 0.866(distanza di ogni cella in verticale)
h_ax.yaxis.set_major_locator(loc)
# qui è stata impostata una distanza di cinque esagoni per ogni tick, la distanza in verticale
# di ogni esagono è di 0.866, 0.866 * 5 = 4.33 == un tick ogni cinque esagoni


#  impostazione dei nomi dei tick
num = [-20, -15, -10, -5, 0, 5, 10, 15]
h_ax.set_yticklabels(num)
h_ax.set_xticklabels(num)
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
