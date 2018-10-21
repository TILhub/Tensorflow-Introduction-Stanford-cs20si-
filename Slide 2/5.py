import tensorflow as tf
W=tf.Variable(tf.truncated_normal([700,10]))
with tf.Session() as sess:
	sess.run(W.initializer)
	#print(sess.run(W))
	print(W.eval())
