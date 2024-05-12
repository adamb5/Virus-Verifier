# VirusVerif
The SEIR model splits out the infected population into two sub-groups, those who are infected but not yet contagious and those who are infectious. The SEIR model is very similar to the SIR model, but susceptible people who become infected first move into the exposed group (E). An additional parameter,  𝜖 , controls how long a person stays in the exposed group before they move into the infectious state.

When no vaccine is available, the isolation of diagnosed infected and social distancing are the only control measures available. In the SEIR model, the governing differential equations are

𝑑𝑆/𝑑𝑡=Λ−𝛽𝑆(𝑡)𝐼(𝑡)𝑁(𝑡)−𝜇𝑆(𝑡),Eq.(7)
 
𝑑𝐸/𝑑𝑡=𝛽𝑆(𝑡)𝐼(𝑡)𝑁(𝑡)−(𝜇+𝜖)𝐸(𝑡),Eq.(8)
 
𝑑𝐼/𝑑𝑡=𝜖𝐸(𝑡)−(𝛾+𝜇+𝛼)𝐼(𝑡),Eq.(9)
 
𝑑𝑅/𝑑𝑡=𝛾𝐼(𝑡)−𝜇𝑅(𝑡),Eq.(10)
 
where the parameters are defined as

Λ
 : Per-capita birth rate.

𝜇
 : Per-capita natural death rate.

𝛼
 : Virus-induced average fatality rate.

𝛽
 : Probability of disease transmission per contact times the number of contacts per unit time.

𝜖
 : Rate of progression from exposed to infectious (the reciprocal is the incubation period).

𝛾
 : Recovery rate of infectious individuals (the reciprocal is the infectious period).

In this model, assumed that the birth and death rate are different and governed by the two parameters  Λ
  and  𝜇
 . Additionally, the total number of the population is not constant but it depends on time.

𝑁(𝑡)=𝑆(𝑡)+𝐸(𝑡)+𝐼(𝑡)+𝑅(𝑡),
 
with an initial condition

𝑁(0)=𝑁0.
 
The number of deaths (both from the disease and natural causes) can be evaluated as follows

𝐷(𝑡)=𝑁0−𝑁(𝑡),
 
from which we can evaluate the deaths per unit time, that is

𝑑𝐷/𝑑𝑡=−(𝑑𝑆/𝑑𝑡+𝑑𝐸/𝑑𝑡+𝑑𝐼/𝑑𝑡+𝑑𝑅/𝑑𝑡).
 
The basic reproductive factor is in this case (see, e.g., Diekmann, Odo, Heesterbeek, Hans and Britton, Tom. Mathematical Tools for Understanding Infectious Disease Dynamics, Princeton: Princeton University Press, 2012. https://doi.org/10.1515/9781400845620)

𝑅0=𝛽𝜖/(𝜖+𝜇)(𝛾+𝜇+𝛼)
