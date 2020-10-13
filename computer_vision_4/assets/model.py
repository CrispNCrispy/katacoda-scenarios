def create_model():
	model = tf.keras.Sequential([
    		tf.keras.layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32,32,1)),
    		tf.keras.layers.AveragePooling2D(),
    		tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),
    		tf.keras.layers.AveragePooling2D(),
    		tf.keras.layers.Flatten(),
    		tf.keras.layers.Dense(units=120, activation='relu'),
    		tf.keras.layers.Dense(units=84, activation='relu'),
    		tf.keras.layers.Dense(units=10, activation='softmax')
		])
	return model
