A. Conclusions
1. It is ideal to have 2 Convolution layers for this algorithm: Less than 2 will drastically decrease the accuracy while over 2 has little to no effect and just increases the runtime.

2. The number of filters for the Convolution layers should be around 32: Having more has little to no effect and just increases the runtime, while having less noticably decreases the accuracy.

3. If using more than one dense hidden layer, the dropout rates should be lower: I suspect this is because too many dropouts across too many layers cause too much chaos. Perhaps could be solved with a bigger data set.

4. For this case, a single dense hidden layer is not only sufficient but also desirable: Anything more actually just decreases the accuracy.

5. The best model that I found can be found at C-12 below (and my submitted code).

B. Experimentation Process

I started my base model entirely based on handwriting.py porvided during the lecture. It is depicted on C-1 below. The initial accruracy was extremely low, being only 0.0564.

Then I added a Convolution layer which increased the accracy drastically to 0.9644.

Adding a MaxPooling layer on top of that did almost no change and only decreased the loss by a small amount.

Then I added another dense hidden layer with a dropout rate of 0.5, which decreased the accuracy to 0.7165.

Removing a Convolution layer & a MaxPooling layer at this point again drastically decreased the accuracy, so I immediately added it back in.

Then I started to fiddle with the dropout rate (still with 2x dense hidden layers). As it turns out, having too high of a dropout rate drastically decreased the accuracy and the optimal dropout rate is around 0.1.

Then I went back and deleted the extra dense hidden layer and started to fiddle with the dropout layer again (so this time, only with dens hidden layer). As it turns out, this time, the optimal dropout rate is around 0.3.

So, having the number of hidden layers set to 1 and the dropout rate set to 0.3, I have changed the number of filters for the Convolution layer. As it turns out, 32 was a pretty good number to begin with.

C. Models
1.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.5)
} = loss: 3.4968 - accuracy: 0.0564

2.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	Flatten
	Dense(128, relu)
	Dropout(0.5)
} = loss: 0.1568 - accuracy: 0.9644

3.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2,2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.5)
} = loss: 0.1263 - accuracy: 0.9644

4.
{
	Conv2D(32, (5, 5), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (5, 5), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.5)
} = loss: 0.2827 - accuracy: 0.9237

5.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.5)
	Dense(128, relu)
	Dropout(0.5)
} = loss: 0.8988 - accuracy: 0.7165

6. 
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.2)
	Dense(128, relu)
	Dropout(0.2)
} = loss: 3.4975 - accuracy: 0.0550

7. 
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.2)
	Dense(128, relu)
	Dropout(0.2)
} = loss: 0.1882 - accuracy: 0.9512

8.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.9)
	Dense(128, relu)
	Dropout(0.9)
} = loss: 3.4949 - accuracy: 0.0571


9.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.4)
	Dense(128, relu)
	Dropout(0.4)
} = loss: 0.3146 - accuracy: 0.9076

10. 
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.1)
	Dense(128, relu)
	Dropout(0.1)
} = loss: 0.2141 - accuracy: 0.9545

11.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.1)
} = loss: 0.2514 - accuracy: 0.9495

12.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.3)
} = loss: 0.1337 - accuracy: 0.9703

13.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.4)
} = loss: 0.1469 - accuracy: 0.9612

14.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.2)
} = loss: 0.2145 - accuracy: 0.9528

15.
{
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(32, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.3)
} = loss: 0.1893 - accuracy: 0.9533

16.
{
	Conv2D(64, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(64, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.3)
} = loss: 0.1858 - accuracy: 0.9520

17.
{
	Conv2D(16, (3, 3), relu)
	MaxPooling2D(2, 2)
	Conv2D(16, (3, 3), relu)
	MaxPooling2D(2, 2)
	Flatten
	Dense(128, relu)
	Dropout(0.3)
} = loss: 0.2196 - accuracy: 0.9413