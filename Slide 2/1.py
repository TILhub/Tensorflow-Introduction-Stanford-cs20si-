import tensorflow as tf
a=tf.constant(2)
b=tf.constant(3)

# a=tf.constant(2,name='a')
# b=tf.constant(3,name='b')
# to add name to constants to tensors for tensorboard
x=tf.add(a,b,name='ADD')
writer = tf.summary.FileWriter('./graph',tf.get_default_graph())
with tf.Session() as sess:
	#writer = tf.summary.FileWriter('./graph',tf.graph())
	print(sess.run(x))
writer.close()


# to use tensorboard
# python3 1.py
# tensorboard --logdir="./graph' --port 6006
# u can use any port 

# open any web browser and type this address
# http://localhost:6006
