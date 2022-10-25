# CSI CHICAGO

<center>
<img src=./images/chicago_skyline.jpg alt="crime_scene" width=“400”/>
</center>


## Abstract
The goal of this project is to perform an anlysis of crime in Chicago since 2001 using the data provided by the Chicago Police Departmen through the API of Chicago Data Portal.

This information has been merged with the hardship index by community area to search for correlations between crime and social situation, provided by the Chicago Data Portal aswell.

The location of Police Stations in Chicago has been retrieved from the same source too for plotting interests.

## Considerations

- Around 7.5 million records.
- API was very slow.

## Results

### Total Crimes

After aggregating the dataset it can easily noticed that tht theft and battery are the most popular crimes, with some surprising appearances such as "ritualism".

<center>
<img src=./images/total_crime.png alt="crime_scene" width=“400”/>
</center>

### Correlation of crime and hardship index
The hardship index is an indicator of how harsh are the social an economic conditions of a determinated zone. It encapsules a series of indexes such as the percent of households below poverty, the percent of population aged 16+ unemployed, the percent of population aged 25+ without high school diploma and the per capita income.

<center>
<img src=./images/correlation.png alt="crime_scene" width=“400”/>
</center>

It can be noticed how crimes such as weapons biolation or homicide have a positive correlation with the hardship index.

It is interesting to see that theft is slightly negatively correlated with hardship index, so thiefs prefer to rob in a richer neighborhood (surprise!).

### Police Station distribution

Will the presence of a police stations affect crime distribution?

<center>
<img src=./images/police_stations.png alt="crime_scene" width=“400”/>
</center>

### Police Stations vs. Crime

The answer is.... NO!!

Police Stations don't seem to affect crime distribution at all.

<center>
<img src=./images/crimes_police_stations.png alt="crime_scene" width=“400”/>
</center>

### Police Stations vs. Homicides

Taking into consideration only the homicides it can be noticed that police stations don't seem to disturb them.

A zone of high homicide density can be observed too.

<center>
<img src=./images/homicides_police_stations.png alt="crime_scene" width=“400”/>
</center>

### Police Stations vs. Prostitution

Prostitution seems to be limited to some zones/streets.

<center>
<img src=./images/prostitution_police_stations.png alt="crime_scene" width=“400”/>
</center>

### Police Stations vs. Narcotics

Narcotic related crime seems to be omnipresent.

<center>
<img src=./images/narcotics_police_stations.png alt="crime_scene" width=“400”/>
</center>

### Lets finish with some heatmaps
There is clearly a zone you dont want to step!

<center>
Homicide Heatmap
</center>
<center>
<img src=./images/heatmap_homicides.png alt="crime_scene" width=“400”/>
</center>

The theft heatmat reveals that thetf is evenly distributed but there is a very dark spot.
As a curiosity it is near the Four Seasons Chicago Hotel.

<center>
Theft Heatmap
</center>

<center>
<img src=./images/heatmap_theft.png alt="crime_scene" width=“400”/>
</center>

The narcotics are omnipresent too and have a higher presence in a concrete zone.

<center>
Narcotics Heatmap
</center>
<center>
<img src=./images/heatmap_narcotics.png alt="crime_scene" width=“400”/>
</center>

Vehicle theft has two higher density zones. One of them is repeated from previus charts but there is an additional one in the south.

<center>
Motor Vehicle Theft Heatmap
</center>
<center>
<img src=./images/heatmap_gta.png alt="crime_scene" width=“400”/>
</center>

Porsitution heatmap loses accuracy compared to the plot above the map.

<center>
Prostitution Heatmap
</center>
<center>
<img src=./images/heatmap_prostitution.png alt="crime_scene" width=“400”/>
</center>

# Conclusions

Embrace thug life or leave!