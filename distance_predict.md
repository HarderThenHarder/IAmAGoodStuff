<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

## Distance Predict with Bino-Camera
---
### 1. What is the problem?
What is the distance between object and us? Here is the picture to show what we need to compute. Left frame and Right frame express the left-view and right-view of a bino-camera( or two cameras ). The top `black` object is the our measuring `target`, while the (x1, y1) and (x2, y2) are the `cross points` between `frame` and `the line of target to camera`. Besides, `dL` is the `gap` between `left-camera` and `right-camera`, this value must be known before we start to calculate. The distance we need to figure out is the `d`, which is the vertical line in the center.<br><br>
<img src="assets/distance_predict_image.jpg">

### 2. Solve this problem
#### dL
The `dL` we are already know, so we want to use this value to compute the result of `d`. First, we build the equation set:<br><br>
$dL = x_1 + x_2$<br>
$x_1 = d \times \frac{1}{\tan\alpha_1}$<br>
$x_2 = d \times \frac{1}{\tan\alpha_2}$<br>
<br>
So we can infer that&nbsp; 
$\rightarrow d = \frac{dL}{{\frac{1}{\tan\alpha_1}} + {\frac{1}{\tan\alpha_2}}}$. Now the question is: how to express the $\tan\alpha_1$ and $\tan\alpha_2$? To solve this problem, we need to use vector $\overrightarrow{p_1}$ and vector $\overrightarrow{p_2}$.<br><br>

#### tanα
Note that $\overrightarrow{u_1}$ and $\overrightarrow{u_2}$ are unit vector( which length equals 1). Use the law of cosines, we can get that: 
$\cos\alpha_1 = \frac{\overrightarrow{p_1} \cdot \overrightarrow{u_1}}{|\overrightarrow{p_1}|\times|\overrightarrow{u_1}|} = \frac{\overrightarrow{p_1} \cdot \overrightarrow{u_1}}{|\overrightarrow{p_1}|}$, where $\overrightarrow{p_1} = (x, y, d'), \overrightarrow{u_1} = (1, 0, 0)$ . <br><br>
*The most important is: `d'` is the `focal length in px`, not in mm!*<br><br>
So $\cos\alpha_1 = \frac{x}{\sqrt{x^2 + y^2 + d'^2}}$, same as $\cos\alpha_2$.<br><br>
Now we can express the $\tan\alpha$ using the $\cos\alpha$. <br><br>
$\tan\alpha = \sqrt{\frac{1}{\cos\alpha^2} - 1} \rightarrow \tan\alpha_1 = \sqrt{\frac{x^2 + y^2 + d'^2}{x^ 2} - 1} = \sqrt{\frac{y^2 + d'^2}{x^2}}$
<br><br>

#### d'
As I said, d' is the focal length in `px` unit, not in mm. Because we express the $\overrightarrow{p_1}$ in (x, y, d'), the x and y are the `pixel` unit, so the d' must use the same unit. To calculate the d', we need to know the FOV(Filed of view), noted by $\beta$ in top picture. Since we know the *width* and *height* of our frame, we can calculate d'.<br><br>
$\tan{\frac{\beta}{2}} = \frac{\frac{width}{2}}{d'} \rightarrow d' = \frac{width}{2\tan\frac{\beta}{2}}$<br><br>

#### Result
Finally we can draw the conclusion of d:<br><br>
$d = \frac{dL}{\frac{1}{\sqrt{\frac{y_1^2 + d'^2}{x_1^2}}} + \frac{1}{\sqrt{\frac{y_2^2 + d'^2}{x_2^2}}}} \qquad , \qquad d'= \frac{width}{2\tan\frac{\beta}{2}}$<br><br>
Where $x1, y1$ are the coordinate in the left frame, while $x2, y2$ are the coordinate in the right frame.