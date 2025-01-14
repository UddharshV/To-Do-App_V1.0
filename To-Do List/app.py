from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__,template_folder="templates")

to_do_list=[{"Activity":"Sample Activity 1","Status":True}]

@app.route("/")
def index():
    return render_template("index.html",to_do_list=to_do_list)

@app.route("/add",methods=["POST"])
def add():
    task=request.form['task']
    to_do_list.append({"Activity":task,"Status":False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>",methods=["GET","POST"])
def edit(index):
    task=to_do_list[index]
    if request.method == "POST":
        task['Activity']=request.form['task']
        return redirect(url_for("index"))
    else:
        return render_template("edit.html",to_do_list=to_do_list,index=index)
    
@app.route("/check/<int:index>")
def check(index):
    to_do_list[index]["Status"] = not to_do_list[index]["Status"]
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del to_do_list[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)