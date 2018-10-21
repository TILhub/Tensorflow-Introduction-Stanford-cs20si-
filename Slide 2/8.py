import tensorflow as tf
my_var=tf.Variable(10)
with tf.Session() as sess:
	sess.run(my_var.initializer)
	
	sess.run(my_var.assign_add(10))
	print(my_var.eval())
	sess.run(my_var.assign_sub(2))
	print(my_var.eval())
