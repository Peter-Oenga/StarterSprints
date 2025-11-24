package com.example.widgetimageslider;

import android.appwidget.AppWidgetManager;
import android.content.ComponentName;
import android.util.Log;
import android.widget.RemoteViews;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {

    @Override
    public void onNewToken(String token) {
        super.onNewToken(token);
        Log.d("FCM", "✅ New token received: " + token);
    }

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);

        Log.d("FCM", "✅ Push received successfully");

        try {
            AppWidgetManager manager = AppWidgetManager.getInstance(this);
            ComponentName widget = new ComponentName(this, ImageSliderWidget.class);
            int[] ids = manager.getAppWidgetIds(widget);

            RemoteViews views = new RemoteViews(getPackageName(), R.layout.image_slider_widget);

            // Demo text for client visibility
            views.setTextViewText(R.id.demoStatus, "✅ Updated via push notification!");

            for (int id : ids) {
                manager.updateAppWidget(id, views);
            }

            Log.d("FCM", "✅ Widget refreshed");

        } catch (Exception e) {
            Log.e("FCM", "❌ Error updating widget: " + e.getMessage());
        }
    }
}
