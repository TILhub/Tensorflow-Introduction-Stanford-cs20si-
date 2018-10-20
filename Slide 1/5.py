import tensorflow as tf
#create a graph
g=tf.Graph()
# set this grah as default to add operators
with g.as_default():
	x=tf.add(3,5)
sess=tf.Session(graph=g)
with tf.Session(graph=g) as sess:
	x=sess.run(x)
	print(x)
