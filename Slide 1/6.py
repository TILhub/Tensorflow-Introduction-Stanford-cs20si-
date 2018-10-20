import tensorflow as tf
#create a graph
g=tf.Graph()

#add ops to default graph
a=tf.constant(3.14)

#add to user created graph g
with g.as_default():
	b=tf.constant(2.71)
#passing data vetween both the graphs is not possible
