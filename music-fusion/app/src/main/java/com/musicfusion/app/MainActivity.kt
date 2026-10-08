package com.musicfusion.app

import android.graphics.Color
import android.net.Uri
import android.os.Bundle
import android.view.ViewGroup
import android.widget.Button
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.browser.customtabs.CustomTabsIntent

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val root=LinearLayout(this).apply {
            orientation=LinearLayout.VERTICAL
            setPadding(32,48,32,24)
            setBackgroundColor(Color.rgb(9,11,22))
        }
        root.addView(TextView(this).apply {
            text="Music Fusion"; textSize=30f; setTextColor(Color.WHITE)
        })
        root.addView(TextView(this).apply {
            text="AI Music Studio"; textSize=16f; setTextColor(Color.LTGRAY)
            setPadding(0,8,0,32)
        })
        addButton(root,"Open Suno","https://suno.com")
        addButton(root,"Open Flow Music",BuildConfig.FLOW_MUSIC_URL)
        setContentView(root)
    }
    private fun addButton(parent:LinearLayout,label:String,url:String){
        val b=Button(this).apply {
            text=label
            setOnClickListener {
                CustomTabsIntent.Builder().build().launchUrl(this@MainActivity,Uri.parse(url))
            }
        }
        parent.addView(b,LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,ViewGroup.LayoutParams.WRAP_CONTENT).apply{bottomMargin=14})
    }
}