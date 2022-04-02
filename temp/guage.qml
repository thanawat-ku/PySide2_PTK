import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
Rectangle {
  id: main
  width: 512
  height: 512
  color: 'black'

  // Put some text in the background just to check opacity
  Text {
    x: main.width/6.0-0.5*contentWidth
    y: main.height/2.0-0.5*contentHeight
    text: '30'
    color: 'white'
  }
  Text {
    x: main.width/2.0-0.5*contentWidth
    y: main.height/6.0-0.5*contentHeight
    text: '60'
    color: 'white'
  }
  Text {
    x: 5.0*main.width/6.0-0.5*contentWidth
    y: main.height/2.0-0.5*contentHeight
    text: '90'
    color: 'white'
  }

  // Shader effect to provide gradient-based gauge
  ShaderEffect {
    id: gauge
    anchors.fill: parent

    opacity: 0.75  // Making it totally opaque on leading edge obscures the number!

    // Angles measured clockwise from up, in range -pi to pi
    property real angleBase: -pi*0.75
    property real angle

    readonly property real pi: 3.1415926535897932384626433832795

    vertexShader: "
      uniform highp mat4 qt_Matrix;
      attribute highp vec4 qt_Vertex;
      attribute highp vec2 qt_MultiTexCoord0;
      varying highp vec2 coord;
      void main() {
        coord = qt_MultiTexCoord0;
        gl_Position = qt_Matrix * qt_Vertex;
      }"

    fragmentShader: "
      uniform lowp float qt_Opacity;
      uniform highp float angleBase;
      uniform highp float angle;
      varying highp vec2 coord;
      void main() {
        gl_FragColor = vec4(0.0,0.0,0.0,0.0);
        highp vec2 d=2.0*coord-vec2(1.0,1.0);
        highp float r=length(d);
        if (0.25<=r && r<=0.75) {
          highp float a=atan2(d.x,-d.y);
          if (angleBase<=a && a<=angle) {
            highp float p=(a-angleBase)/(angle-angleBase);
            gl_FragColor = vec4(0.0,0.0,p,p) * qt_Opacity;
          }
        }
      }"
  }

  // Animate the gauge position
  SequentialAnimation {
    running: true
    loops: Animation.Infinite
    NumberAnimation {
      from: gauge.angleBase
      to: gauge.angleBase+1.5*gauge.pi
      duration: 1000
      target: gauge
      property: 'angle'
      easing.type: Easing.InOutSine
    }
    NumberAnimation {
      from: gauge.angleBase+1.5*gauge.pi
      to: gauge.angleBase
      duration: 1000
      target: gauge
      property: 'angle'
      easing.type: Easing.InOutSine
    }
  }
}
}