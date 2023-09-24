import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/spot")
def spot():
    return render_template("spot.html")

@app.route("/rest")
def rest():
    return render_template("rest.html")

@app.route("/food/<int:grp_flg>")
def foodList(grp_flg):

    conn = sqlite3.connect("local_trip.db")
    c = conn.cursor()
    c.execute("select place_name, place_img_ent from place where grp_flg = ?", (grp_flg,))
    place_list = c.fetchall()
    place_name = place_list[0][0]
    place_img_ent = place_list[0][1]
    place_name2 = place_list[1][0]
    place_img_ent2 = place_list[1][1]
    place_name3 = place_list[2][0]
    place_img_ent3 = place_list[2][1]
    c.close()

    return render_template(
        "food.html",
        place_name = place_name,
        place_img_ent = place_img_ent,
        place_name2 = place_name2,
        place_img_ent2 = place_img_ent2,
        place_name3 = place_name3,
        place_img_ent3 = place_img_ent3
        )

@app.route("/rest/<int:grp_flg>")
def restList(grp_flg):

    conn = sqlite3.connect("local_trip.db")
    c = conn.cursor()
    c.execute("select place_name, place_img_ent from place where grp_flg = ?", (grp_flg,))
    place_list = c.fetchall()
    print(place_list)
    place_name = place_list[0][0]
    place_img_ent = place_list[0][1]
    place_name2 = place_list[1][0]
    place_img_ent2 = place_list[1][1]
    place_name3 = place_list[2][0]
    place_img_ent3 = place_list[2][1]
    c.close()

    return render_template(
        "rest.html",
        place_name = place_name,
        place_img_ent = place_img_ent,
        place_name2 = place_name2,
        place_img_ent2 = place_img_ent2,
        place_name3 = place_name3,
        place_img_ent3 = place_img_ent3
        )

@app.route("/spot/<int:grp_flg>")
def spotList(grp_flg):

    conn = sqlite3.connect("local_trip.db")
    c = conn.cursor()
    c.execute("select place_name, place_img_ent from place where grp_flg = ?", (grp_flg,))
    place_list = c.fetchall()
    print(place_list)
    place_name = place_list[0][0]
    place_img_ent = place_list[0][1]
    place_name2 = place_list[1][0]
    place_img_ent2 = place_list[1][1]
    place_name3 = place_list[2][0]
    place_img_ent3 = place_list[2][1]
    c.close()

    return render_template(
        "spot.html",
        place_name = place_name,
        place_img_ent = place_img_ent,
        place_name2 = place_name2,
        place_img_ent2 = place_img_ent2,
        place_name3 = place_name3,
        place_img_ent3 = place_img_ent3
        )


@app.route("/detail/<int:id>")
def detail(id):

    conn = sqlite3.connect("local_trip.db")
    c = conn.cursor()
    c.execute("select place_name, address, tel_number, map, place_img_ent, place_img_con, place_img_in, text, place_url, place_time, holiday from place where id = ?", (id,))
    place_info = c.fetchall()[0]
    place_name = place_info[0]
    address = place_info[1]
    tel_number = place_info[2]
    map = place_info[3]
    place_img_ent = place_info[4]
    place_img_con = place_info[5]
    place_img_in = place_info[6]
    text = place_info[7]
    place_url = place_info[8]
    place_time = place_info[9]
    holiday = place_info[10]
    c.close()
    
    return render_template(
        "detail.html",
        place_name = place_name,
        address = address,
        tel_number = tel_number,
        map = map,
        place_img_ent = place_img_ent,
        place_img_con = place_img_con,
        place_img_in = place_img_in,
        text = text,
        place_url = place_url,
        place_time = place_time,
        holiday = holiday
        )

if __name__ == "__main__":
    app.run(debug=True)
