package com.example.widgetimageslider;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.StrictMode;
import android.widget.RemoteViews;

import org.json.JSONArray;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ImageSliderWidget extends AppWidgetProvider {

    private static final String ACTION_NEXT = "com.example.widgetimageslider.NEXT";
    private static final String API_URL = "https://euafroawards.com/assets/api.php";

    @Override
    public void onUpdate(Context context, AppWidgetManager manager, int[] widgetIds) {
        for (int widgetId : widgetIds) {
            updateWidget(context, manager, widgetId);
            startAutoSlide(context, widgetId);
        }
    }

    private void updateWidget(Context context, AppWidgetManager manager, int widgetId) {

        StrictMode.ThreadPolicy policy =
                new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        RemoteViews views = new RemoteViews(context.getPackageName(), R.layout.image_slider_widget);

        try {
            JSONArray json = getImagesFromApi();
            if (json.length() == 0) return;

            SharedPreferences prefs = context.getSharedPreferences("slider_prefs", Context.MODE_PRIVATE);
            int index = prefs.getInt("index_" + widgetId, 0);

            if (index >= json.length()) index = 0;

            String imageUrl = json.getJSONObject(index).getString("file_name");

            Bitmap bmp = downloadBitmap(imageUrl);
            if (bmp != null) {
                views.setImageViewBitmap(R.id.widget_image, bmp);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        // NEXT button (incomplete old version)
        Intent nextIntent = new Intent(context, ImageSliderWidget.class);
        nextIntent.setAction(ACTION_NEXT);
        nextIntent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, widgetId);

        PendingIntent nextPending = PendingIntent.getBroadcast(
                context,
                widgetId,
                nextIntent,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_MUTABLE
        );

        views.setOnClickPendingIntent(R.id.button_next, nextPending);
        manager.updateAppWidget(widgetId, views);
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        super.onReceive(context, intent);

        if (!ACTION_NEXT.equals(intent.getAction())) return;

        int widgetId = intent.getIntExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, -1);
        if (widgetId == -1) return;

        try {
            JSONArray json = getImagesFromApi();

            SharedPreferences prefs = context.getSharedPreferences("slider_prefs", Context.MODE_PRIVATE);
            int index = prefs.getInt("index_" + widgetId, 0);
            index = (index + 1) % json.length();
            prefs.edit().putInt("index_" + widgetId, index).apply();

            AppWidgetManager manager = AppWidgetManager.getInstance(context);
            updateWidget(context, manager, widgetId);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void startAutoSlide(Context context, int widgetId) {
        AlarmManager alarmManager =
                (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);

        Intent intent = new Intent(context, ImageSliderWidget.class);
        intent.setAction(ACTION_NEXT);
        intent.putExtra(AppWidgetManager.EXTRA_APPWIDGET_ID, widgetId);

        PendingIntent pendingIntent = PendingIntent.getBroadcast(
                context,
                widgetId,
                intent,
                PendingIntent.FLAG_UPDATE_CURRENT | PendingIntent.FLAG_MUTABLE
        );

        alarmManager.setRepeating(
                AlarmManager.RTC_WAKEUP,
                System.currentTimeMillis() + 5000,
                5000,
                pendingIntent
        );
    }

    private JSONArray getImagesFromApi() throws Exception {
        URL url = new URL(API_URL);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        InputStream in = conn.getInputStream();

        StringBuilder sb = new StringBuilder();
        int c;
        while ((c = in.read()) != -1) {
            sb.append((char) c);
        }

        return new JSONArray(sb.toString());
    }

    private Bitmap downloadBitmap(String src) {
        try {
            URL url = new URL(src);
            HttpURLConnection connection =
                    (HttpURLConnection) url.openConnection();
            connection.connect();
            InputStream input = connection.getInputStream();
            return BitmapFactory.decodeStream(input);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
