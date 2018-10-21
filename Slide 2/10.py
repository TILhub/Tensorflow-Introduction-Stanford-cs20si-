import tensorflow as tf

# tf.placeholder(dtype, shape=None, name=None)

a=tf.placeholder(tf.float32,shape=[3])

b=tf.constant([5,5,5], tf.float32)

c=a+b

with tf.Session() as sess:
	print(sess.run(c, feed_dict={a:[1,2,3]}))
	
	
# for multiple values
# with tf.Session() as sess:
#	for a_value in list_of_values:
#		print(sess.run(c,{a:a_value}))	
	
	
# There's not much related between tf.Variable and tf.placeholder in my opinion. You use a Variable if you need to store state. You use a placeholder if you need to input external data.
