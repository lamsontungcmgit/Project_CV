package com.example.demoiot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class MainActivity extends AppCompatActivity {

    MQTTHelper mqttHelper;
    TextView txtTemp, txtHumi;
    TextView txtDoor;
    LabeledSwitch  btnLED, btnPUMP, btnSENSOR;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtTemp = findViewById(R.id.txtTemperature);
        txtHumi = findViewById(R.id.txtHumidity);
        txtDoor = findViewById(R.id.tv_Door);
        btnLED = findViewById(R.id.btnLED);
        btnPUMP = findViewById(R.id.btnPUMP);
        btnSENSOR =findViewById(R.id.btnSENSOR);
        btnLED.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("todiuquang123/feeds/nutnhan1","1");
                }else {
                    sendDataMQTT("todiuquang123/feeds/nutnhan1","0");
                }
            }
        });
        btnSENSOR.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("todiuquang123/feeds/nutnhan3","1");
                }else {
                    sendDataMQTT("todiuquang123/feeds/nutnhan3","0");
                }
            }
        });

        btnPUMP.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn) {
                if (isOn == true){
                    sendDataMQTT("todiuquang123/feeds/nutnhan2","1");
                }else {
                    sendDataMQTT("todiuquang123/feeds/nutnhan2","0");
                }
            }
        });


        startMQTT();
    }
    public void sendDataMQTT(String topic, String value){
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }
    }
    public void startMQTT(){
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + "***" +message.toString() );
                if (topic.contains("cambien1")){
                    txtTemp.setText(message.toString()+"℃");
                } else if (topic.contains("cambien2")){
                    txtHumi.setText(message.toString()+"%");
                } else if (topic.contains("nutnhan1")){
                    if (message.toString().equals("1")){
                        btnLED.setOn(true);
                    }else{
                        btnLED.setOn(false);
                    }
                } else if (topic.contains("nutnhan2")){
                    if (message.toString().equals("1")){
                        btnPUMP.setOn(true);
                        txtDoor.setText("Cửa đang mở");
                    }else{
                        btnPUMP.setOn(false);
                        txtDoor.setText("Cửa đang đóng");
                    }
                } else if (topic.contains("nutnhan3")){
                    if (message.toString().equals("1")){
                        btnSENSOR.setOn(true);
                    }else{
                        btnSENSOR.setOn(false);
                    }
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}
