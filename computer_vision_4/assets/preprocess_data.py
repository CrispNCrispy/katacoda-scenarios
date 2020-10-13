def prepare_data(images):
	images  = images / 255.0
	images = np.expand_dims(images,-1)
	images = np.pad(images, ((0,0),(2,2),(2,2),(0,0)), 'constant')
	return images
