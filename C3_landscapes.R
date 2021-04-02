#Lee Przybylski 2/11/2021

library(TDA)
library(ggplot2)

phi0 <- function(x){
  x/3
}
phi0(9)
phi2 <- function(x){
  (x+2)/3
}


scale <- 20 

C3prox <- c(0)
for (j in 1:20){
  out0 <- phi0(C3prox)
  out2 <- phi2(C3prox)
  C3prox <- c(out0, out2)
}
C3prox <- data.frame(matrix(C3prox, nrow = length(C3prox), ncol = 1))
names(C3prox) <- "x"
C3prox$y <- 0
head(C3prox)
ggplot(data = C3prox, aes(x = x, y = y)) + geom_point()

diagram_week <- ripsDiag(C3prox, maxdimension =0, maxscale = msc, library = "Dionysus")

