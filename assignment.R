#.Try to write a code for printing sequence of numbers from 1 to 50 with the differences of 3, 5, 10 

x<-seq(1,50,3)
x
y<-seq(1,50,5)
y
z<-seq(1,50,10)
z
#2.What are the different data objects in R? and write syntax and example for each and every object
#Vectors
#Lists
#Matrices
#Arrays
#Factors
#Data Frames

#1.Vectors
x<-c(1,2,3,4,5)
x


#2.Lists

out_list <- list(2,3,4)
out_list


#3.materices

mat <- matrix (  c(2 , 4, 3, 1, 5, 7) ,
  nrow =2,                  
  ncol =3,                  
  byrow = TRUE)

mat

#4.arrays

x <- c(2,9,3)
y <- c(10,16,17,13,11,15)
result <- array(c(x,y),dim = c(3,3,2))
print(result)

#5.factors

directions <- c("North", "North", "West", "South")
factor(directions)

#6.dataframes

int_vec <- c(1,2,3) 
char_vec <- c("a", "b", "c")
bool_vec <- c(TRUE, TRUE, FALSE)
data_frame <- data.frame(int_vec, char_vec,  bool_vec)
data_frame



#4.
x <- -3
if (x == 0) {
  print("Zero")
} else if (x > 0) {
  print("Positive number")
} else print("Negative Number")

x<- 10
if(x == 0){
  print("zero")
}else if(x > 0){
  print("Positive number")
}el


#5.
x<- 1
class(x)
y<-c("Rohit")
class(y)
z<-7L
class(z)



#write difference between break and next also write examples for both 

# Loop Control Statements
# break Statement - terminates the loop statement and transfers execution to the statement 
# immediately following the loop
v <- c("Rohit","Gaikwad")
cnt <- 2

repeat {
  print(v)
  cnt <- cnt + 1
  
  if(cnt > 5) {
    break
  }
}


# next Statement - useful when we want to skip the current iteration of a loop without terminating it
v <- LETTERS[1:10]
for ( i in v) {
  
  if (i == "D") {
    next
  }
  print(i)
}



#7.write a program to print a given vector in reverse format  

x= c(1,5.6,3,10,3.5,5)
x
t(x)
z<-rev(x)
z




x<-c ("'a','b','c','t','a','c','r','a','c','t','z','r','v','t','u','e','t'")
library(modeest)


?mode

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}



charv <- c ("a","b","c","t","a","c","r","a","c","t","z","r","v","t","u","e","t")


result <- getmode(charv)
print(result)



#Write a function to filter only data belongs to 'setosa' in species of Iris dataset.( using dplyr package) 
iris <- datasets::iris
iris

library(dplyr)

View(iris)
View(filter(iris, Species == 'setosa'))


#10.Create a new column for iris dataset with the name of Means_of_obs, which contains mean value of each row.( using dplyr package)
iris3 = mutate(iris, Means_of_obs = (Sepal.Length + Sepal.Width + Petal.Length + Petal.Width) / 4)

View(iris3)

#Filter data for the "versicolor" and get only 'sepel_length' and Sepel _width' columns.( using dplyr package)
View(select(filter(iris,Species == 'versicolor'), 'sepal_length', 'sepal_width')))
d %>%select(sepal_length, sepal_width)  %>% filter(iris,Species == 'versicolor') 

View(d)






