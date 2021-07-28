def save(self):
	super().save()

	img = Image.open(self.image.path)


	w = img.width
	h = img.height

	if h > w:
		left = 0
		right = w
		top = (h - w)/2
		bottom = (h + w)/2
		img = img.crop((left, top, right, bottom))
		# Resize the image to 300x300 resolution
		if h > 300 or w >300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	# When image width is greater than its height
	elif w > h:
		# make square by cutting off equal amounts left and right
		left = (w - h)/2
		right = (w + h)/2
		top = 0
		bottom = h
		img = img.crop((left, top, right, bottom))
		# Resize the image to 300x300 resolution
		if h > 300 or w >300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	else: 
		output_size = (300, 300)
		img.thumbnail(output_size)
		img.save(self.image.path)