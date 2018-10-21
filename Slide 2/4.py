import tensorflow as tf
s=tf.get_variable("Scalar",initializer=tf.constant(2))


m=tf.get_variable("Matrix",initializer=tf.constant([[1,2],[3,4]]))

W=tf.get_variable("LargeMat",shape=(10000,1000),initializer=tf.zeros_initializer())

# PS name of a variable cannot have space in between them
#Large mat is an illegal name

# see this 'V' instead of 'v' as Variable is a class not an operation like 
# constant

#	with tf.Session() as sess:
#		print(sess.run(W))
#	Flags error as Variable needs to be initialized first		
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	print(sess.run(W))
