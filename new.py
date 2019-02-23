from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv
import sys

inp = sys.argv[1]
lats = []
longs = []
query1 = 'latitude'
query2 = 'longitude'

def isUnique(inp, measurements):
	for i in measurements:
		if (inp == i):
			return False

	return True

with open('revised_summary_loc.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if(row['arithmetic_mean'] != "0" and row['parameter_name'] == inp):
			lats.append((float)(row[query1]))
			longs.append((float)(row[query2]))

print(len(lats))

map = Basemap(projection='cyl')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua', zorder=0)
map.drawcoastlines()

x, y = map(longs, lats, inverse=True)

map.scatter(x,y)

plt.show()
