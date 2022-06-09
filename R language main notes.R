data()
airquality <- datasets:: airquality
airquality
View(airquality)


# top 10 rows and last 10 row
head(airquality,10)
tail(airquality,10)
head(airquality,5)


#visualisation
plot(airquality$Wind,airquality$Temp)


cor(airquality$Temp,airquality$Wind)


##extract

airquality[,]
airquality[1,]
airquality[1:50,c(1,2)]
airquality[1:5,-c(1,2)]

summary(airquality)

library(moments)
skewness(airquality$Solar.R)
skewness(airquality$Solar.R,na.rm = T)
View(airquality)
mean(airquality$Solar.R,na.rm=T) #na.rm  remove null value




#####
plot(airquality$Wind)
plot(airquality$Solar.R,airquality$Ozone,type ="p")
plot(airquality)

plot(airquality$Wind,type="l") # p = point and l = line
 
plot(airquality$Wind,xlab='ozone conc',ylab='no of inst',main='chart',col='blue')



boxplot(airquality$Wind)

hist(airquality$Solar.R)


#multiple box plots
boxplot(airquality[,1:4],main='multiple')


###dplyr

library(dplyr)



####nycflights

library(nycflights13)
View(flights)
dim(flights) # rows and column

#################################################3
View(filter(flights, month ==1, day == 1))



###############################################3
View(arrange(flights,year,month,day))



##################################################
View(arrange(flights,desc(arr_delay)))



#select column by name
View(select(flights,year,month,day))



#select all column between year and day (inclusive)

View(select(flights,year:day))

#select all column except those from year to day (inclusive)
View(select(flights,-(year:day)))


#create new column

flights1 = mutate(flights,gain = arr_delay-dep_delay,speed = distance / air_time *60)

View(flights1)

#

flight2 = mutate(flights , gain= arr_delay - dep_delay,
gain_per_hr =  gain / air_time/60 )
View(flight2)



###### 
View(sample_n(flights,20))

View(sample_frac(flights, 0.01))

###### group by


destination <- group_by(flight,dest)
summarise(destination,planes = n_distinct(tailnum),flights = n())
View(destination)

daily<- group_by(flights,year,month,day)
(per_day<- summarise(daily,flights=n()))
(per_month <- summarise(per_day,flights=sum(flights)))
(per_year<- summarise(per_month,flights= sum(flights)))


View(daily)

########
View(select(flights,year))
select(flights,1)

######


filter1=filter(
  summarise(select(group_by(flights,year,month,day),arr_delay,dep_delay),arr = mean(arr_delay,na.rm=TRUE),
          dep = mean(dep_delay,na.rm=TRUE),arr>30 | dep>30))

View(filter1)


a=summarise(select(group_by(flights,year,month,day),arr_delay,dep_delay))

View(a)











