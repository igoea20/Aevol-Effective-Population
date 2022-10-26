library(ggmuller)
library(ggplot2)

file_location = "C:/..."
pheno_file = "..."
pop_file = "..."

setwd(file_location)

adjacency_df = read.csv(pheno_file)
pop_df = read.csv(pop_file)


Muller_df <- get_Muller_df(adjacency_df, pop_df)
# The palette with grey:
cbPalette <- c("#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")

plot <- ggplot(Muller_df, aes_string(x = "Generation", y = "Frequency", group = "Group_id", fill = "Identity", colour = "Identity")) +
    geom_area() +
    theme(legend.position = "right") +
    guides(linetype = "none", color = "none") +
    scale_y_continuous(labels = 25 * (0:4), name = "Percentage") +
    scale_fill_manual(values=cbPalette) +
    scale_colour_manual(values=cbPalette) +
  ggtitle("Muller Plot, N=256, P=25%") +
  theme(plot.title = element_text(hjust = 0.5))
plot
