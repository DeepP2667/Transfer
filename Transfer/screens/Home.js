import { StyleSheet, View } from "react-native";
import UploadImage from "../icons/UploadImage";
import UploadFile from "../icons/UploadFile";
import DownloadFile from "../icons/DownloadFile";

const containers = StyleSheet.create({
  screenContainer: {
    marginTop: 200,
  },
  rowContainer: {
    flexDirection: "row",
  },
  baseIconContainer: {
    height: 100,
    width: 100,
    borderRadius: 20,
    alignItems: "center",
    justifyContent: "center",
    margin: 25,
  },
});

const Home = () => {
  return (
    <View style={containers.screenContainer}>
      <View style={containers.rowContainer}>
        <UploadImage baseContainer={containers.baseIconContainer} />
        <UploadFile baseContainer={containers.baseIconContainer} />
      </View>
      <View style={containers.rowContainer}>
        <DownloadFile baseContainer={containers.baseIconContainer} />
      </View>
    </View>
  );
};

export default Home;
