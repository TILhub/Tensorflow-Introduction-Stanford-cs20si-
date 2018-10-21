import tensorflow as tf
# create ensors and ops
a=tf.Variable(1)
b=tf.multiply(a,3)

with tf.Session() as sess:
	print(sess.run(b,feed_dict={a:15}))
	
# prints b*a
# prints 15*3
