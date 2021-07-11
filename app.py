from flask import Flask, redirect, url_for, request , render_template
import os
import sys
import subprocess

app = Flask(__name__)

@app.route('/reset')
def vpn():
        return render_template('reset.html')

@app.route('/resetvpn')
def mvpn():
    return render_template('openvpn.html')

@app.route('/macadd')
def mavpn():
        return render_template('macadd.html')

@app.route('/success/<name>')
def success(name):
        return "QRCODE Reset SuccessFully for user %s" %name

@app.route('/update/<name>')
def macupdate(name):
        return "updated new mac successfully with old mac for user %s" %name

@app.route('/Failure/<name>')
def fail(name):
        return "No QRCODE Reset for user %s" %name

@app.route('/macadd2')
def ma2vpn():
        return render_template('macadd2.html')


@app.route('/reset',methods=['POST','GET'])
def resetvpn():
        if request.method == 'POST':
                vpnname=request.form['VPNNM']
                user=request.form['nm']
                if vpnname == 'vpn1':
                    os.system("sshpass -p \'Password\' ssh -pport user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                elif vpnname == 'vpn2':
                    os.system("sshpass -p \'Password\' ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                elif vpnname == 'vpn3':
                    os.system("sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                elif vpnname == 'vpn4':
                    os.system("sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                elif vpnname == 'vpn5':
                    os.system("sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                elif vpnname == 'vpn6':
                    os.system("sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(user))
                    return redirect(url_for('success',name=user))
                else:
                    return redirect(url_for('fail',name=user))

        else:
                return redirect(url_for('success',name=user))


@app.route('/resetvpn',methods=['POST','GET'])
def resetvpnm():
        if request.method == 'POST':
                vpnname = request.form['VPNNM']
                vpnuser = request.form['nm']
                if vpnname == 'vpn1':
                    os.system("sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(vpnuser))
                    return redirect(url_for('success',name=vpnuser))
                if vpnname == 'vpn2':
                    os.system("sshpass -p Password ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} GoogleAuthRegen" .format(vpnuser))
                    return redirect(url_for('success',name=vpnuser))
        else:
            return redirect(url_for('fail',name=vpnuser))




@app.route('/macadd',methods=['POST','GET'])
def macaddvpn():
        if request.method == 'POST':
                vpnname=request.form['VPNNM']
                user=request.form['nm']
                macad=request.form['mcad']
                if vpnname == 'vpn1':
                    os.system('sshpass -p \'Password\' ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn2':
                    os.system('sshpass -p \'Password\' ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn3':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn4':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn5':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn6':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                else:
                    return redirect(url_for('fail',name=user))

        else:
                return redirect(url_for('updated',name=user))



@app.route('/macadd2',methods=['POST','GET'])
def macadd2vpn():
        if request.method == 'POST':
                vpnname=request.form['VPNNM']
                user=request.form['nm']
                macad=request.form['mcad']
                if vpnname == 'vpn1':
                    os.system('sshpass -p \'Password\' ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn2':
                    os.system('sshpass -p \'Password\' ssh -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn3':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn4':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn5':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                elif vpnname == 'vpn6':
                    os.system('sshpass -p \'Password\' ssh -o StrictHostKeyChecking=no -pPort user@xxx.xxx.xxx.xxx /usr/local/openvpn_as/scripts/sacli -u {} -k "pvt_hw_addr2" -v {} UserPropPut' .format(user,macad))
                    return redirect(url_for('macupdate',name=user))
                else:
                    return redirect(url_for('fail',name=user))

        else:
                return redirect(url_for('updated',name=user))


if __name__ == '__main__':
        app.run(debug=True,host='xxx.xxx.xxx.xxx',port=xxxx)

