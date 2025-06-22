# FOR SINGLE SCATTER VISULIZATION

# plt.scatter(x,y, color='color_name, marker='marker style, label='labe_name)
import matplotlib.pylab as plt

hours_studies =[1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# scatter plot
# plt.scatter(hours_studies, exam_scores, color='green', marker="o", label="Student Data")

plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.title('Relationshipt between Study Time and Exam Score')
plt.legend()
plt.grid(True)
# plt.show()

# FOR MULTIPLE SCATTER VISULIZATION

#plt.scatter(x,y, color='color_name', marker='marker style', label='label nane' )
import matplotlib.pyplot as plt

plt.scatter( [1,2,3], [50,55,60], color='blue', label='Class A') #g1
plt.scatter( [1,2,3], [45,50,52], color='orange', label='Class B') #g2

plt.xlabel('Hours studied' )
plt.ylabel('Exam Score')
plt.title('lomparison of Two Classes' )
plt.legend()
plt.grid(True)
plt.show()
