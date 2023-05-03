from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_subjects = int(request.form['num_subjects'])
        return render_template('main.html', num_subjects=num_subjects)
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        num_subjects = int(request.form['num_subjects'])
        subjects = []
        sgpa = 0
        total_credits = 0
        credit_scored = 0
        for i in range(num_subjects):

            course = request.form.get(f'course{i}')

            credits = request.form.get(f'credits{i}')
            total_credits += eval(credits)
            tutorial = request.form.get(f'tutorial{i}')

            quiz = request.form.get(f'quiz{i}')

            midterm = request.form.get(f'mid_term{i}')

            project = request.form.get(f'project{i}')

            certificate = request.form.get(f'certificate{i}')

            lab = request.form.get(f'lab{i}')

            endterm = request.form.get(f'end_term{i}')

            hackathon = request.form.get(f'hackathon_codathon{i}')

            highest_total = eval(request.form.get(f'highest{i}'))
            
            total = (float(quiz.split(' ')[0]) + float(tutorial.split(' ')[0]) + float(midterm.split(' ')[0]) + float(project.split(' ')[0]) + float(certificate.split(' ')[0]) + float(lab.split(' ')[0]) + float(endterm.split(' ')[0]) + float(hackathon.split(' ')[0]))

            if total > 0.9 * highest_total:
                sg = 10
            elif total > 0.8 * highest_total:
                sg = 9
            elif total > 0.7 * highest_total:
                sg = 8
            elif total > 0.6 * highest_total:
                sg = 7
            elif total > 0.5 * highest_total:
                sg = 6
            sg_total = int(credits)*sg
            credit_scored += sg_total
            subjects.append({'course': course, 'credits': credits, 'tutorial': tutorial, 'quiz': quiz, 'midterm': midterm, 'project': project, 'certificate': certificate, 'lab': lab, 'endterm': endterm, 'hackathon': hackathon, 'total': total, 'sg': sg, 'sg_total': sg_total})
            sgpa = round(credit_scored/total_credits, 2)
        return render_template('results.html', subjects=subjects, sgpa = sgpa)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
