# EXPERIMENT 7 — R SCRIPT: IRIS DATA ANALYSIS AND VISUALIZATION

# 1. Load and inspect the built-in dataset
data(iris)
head(iris)
str(iris)
summary(iris)

# 2. Check dataset dimensions and names
dim(iris)
nrow(iris)
ncol(iris)
names(iris)

# 3. Check missing values
colSums(is.na(iris))

# 4. Basic statistical analysis
mean(iris$Sepal.Length)
median(iris$Sepal.Length)
sd(iris$Sepal.Length)
min(iris$Sepal.Length)
max(iris$Sepal.Length)

# 5. Analyze different species
table(iris$Species)
aggregate(. ~ Species, data = iris, FUN = mean)

# 6A. Histogram
hist(iris$Sepal.Length,
     main = "Histogram of Sepal Length",
     xlab = "Sepal Length",
     col = "lightblue",
     border = "black")

# 6B. Scatter plot
plot(iris$Sepal.Length, iris$Petal.Length,
     main = "Sepal Length vs Petal Length",
     xlab = "Sepal Length",
     ylab = "Petal Length",
     pch = 19,
     col = as.integer(iris$Species))
legend("topleft", legend = levels(iris$Species),
       col = 1:3, pch = 19)

# 6C. Box plot
boxplot(Sepal.Length ~ Species, data = iris,
        main = "Sepal Length by Species",
        xlab = "Species",
        ylab = "Sepal Length")

# 6D. Pie chart — species proportions
species_counts <- table(iris$Species)
pie(species_counts,
    main = "Iris Species Distribution",
    labels = paste(names(species_counts), species_counts))

# 6E. Better visualization — pairs plot
pairs(iris[1:4],
      main = "Pairwise Scatter Plots of Iris Measurements",
      col = as.integer(iris$Species),
      pch = 19)

# 6F. Bar chart
barplot(species_counts,
        main = "Number of Samples per Species",
        xlab = "Species",
        ylab = "Number of Samples",
        col = "lightgreen")
