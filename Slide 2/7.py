import tensorflow as tf
my_var=tf.Variable(2,name="my_var")

my_var_time_two=my_var.assign(2*my_var)

with tf.Session() as sess:
	sess.run(my-var.initializer)
	sess.run(my_var_times_two)
