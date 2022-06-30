import { View } from "react-native";
import Icon from "react-native-vector-icons/FontAwesome5";

const DownloadFile = ({ baseContainer }) => {
  const fileDownloadIcon = (
    <Icon name="file-download" size={60} color="#cdcdcd" />
  );
  return (
    <View style={[baseContainer, { backgroundColor: "#434ebb" }]}>
      {fileDownloadIcon}
    </View>
  );
};

export default DownloadFile;
