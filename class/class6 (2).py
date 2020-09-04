class transcript():

    def transcript_input(self):
        self.name = input('学生的名字：')
        self.english_record = input('英语成绩是多少：')
        self.math_record = input('数学成绩是多少：')

    def transcript_output(self):
        print(self.name+'的成绩单是：')
        print('英语成绩是：'+str(self.english_record))
        print('数学成绩是：'+str(self.math_record))

transcript_a=transcript()
transcript_b=transcript()

transcript_a.transcript_input()
transcript_a.transcript_output()
#实例化类