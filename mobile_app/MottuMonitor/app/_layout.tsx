import React, { useRef, useState } from "react";
import {
  StyleSheet,
  StatusBar,
  View,
  Text,
  TouchableOpacity,
  ActivityIndicator,
} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { WebView } from "react-native-webview";

export default function Layout() {
  // ⚠️ Substitua pelo IP do seu computador (não use localhost)
  const dashboardUrl = "http://192.168.0.184:3000";

  const webViewRef = useRef<WebView | null>(null);
  const [theme, setTheme] = useState<"light" | "dark">("dark");
  const [loading, setLoading] = useState(true);

  const reloadDashboard = () => {
    if (webViewRef.current) {
      webViewRef.current.reload();
    }
  };

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  // 🎨 Paleta de cores global
  const colors =
    theme === "light"
      ? {
          background: "#f1f5f9",
          header: "#0284c7",
          text: "#0f172a",
          button: "#0ea5e9",
          indicator: "#0284c7",
        }
      : {
          background: "#0b1120",
          header: "#1e293b",
          text: "#f8fafc",
          button: "#38bdf8",
          indicator: "#38bdf8",
        };

  return (
    <SafeAreaView style={[styles.container, { backgroundColor: colors.background }]}>
      <StatusBar
        barStyle={theme === "dark" ? "light-content" : "dark-content"}
        backgroundColor={colors.header}
      />

      {/* 🔹 Cabeçalho */}
      <View style={[styles.header, { backgroundColor: colors.header }]}>
        <Text style={[styles.headerText, { color: colors.text }]}>🏍️ Mottu Smart Monitor</Text>

        <View style={styles.actions}>
          {/* Recarregar */}
          <TouchableOpacity
            style={[styles.button, { backgroundColor: colors.button }]}
            onPress={reloadDashboard}
          >
            <Text style={[styles.buttonText, { color: colors.text }]}>⟳</Text>
          </TouchableOpacity>

          {/* Modo claro/escuro */}
          <TouchableOpacity
            style={[styles.button, { backgroundColor: colors.button }]}
            onPress={toggleTheme}
          >
            <Text style={[styles.buttonText, { color: colors.text }]}>
              {theme === "light" ? "🌙" : "☀️"}
            </Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* 🔹 Conteúdo principal (WebView + Loader) */}
      <View style={[styles.webContainer, { backgroundColor: colors.background }]}>
        {loading && (
          <ActivityIndicator
            size="large"
            color={colors.indicator}
            style={{ marginTop: 40 }}
          />
        )}

        <WebView
          ref={webViewRef}
          source={{ uri: dashboardUrl }}
          style={{ flex: 1, backgroundColor: colors.background }}
          startInLoadingState
          javaScriptEnabled
          domStorageEnabled
          onLoadEnd={() => setLoading(false)}
          injectedJavaScript={`
            document.body.style.backgroundColor = '${colors.background}';
            document.body.style.color = '${colors.text}';
          `}
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    paddingVertical: 14,
    paddingHorizontal: 16,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    elevation: 4,
  },
  headerText: {
    fontSize: 17,
    fontWeight: "bold",
  },
  actions: {
    flexDirection: "row",
    gap: 8,
  },
  button: {
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 8,
  },
  buttonText: {
    fontWeight: "bold",
    fontSize: 16,
  },
  webContainer: {
    flex: 1,
  },
});
