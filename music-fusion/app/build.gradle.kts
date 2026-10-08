plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}
android {
    namespace="com.musicfusion.app"
    compileSdk=35
    defaultConfig {
        applicationId="com.musicfusion.app"
        minSdk=26
        targetSdk=35
        versionCode=1
        versionName="1.0"
        buildConfigField("String","FLOW_MUSIC_URL","\"https://flowmusic.ai\"")
    }
    buildFeatures { buildConfig=true }
}
dependencies {
    implementation("androidx.core:core-ktx:1.15.0")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.activity:activity-ktx:1.10.0")
    implementation("androidx.browser:browser:1.8.0")
}