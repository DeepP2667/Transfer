import { StyleSheet, View } from "react-native";
import Icon from "react-native-vector-icons/FontAwesome5";

const UploadFile = ({ baseContainer }) => {
  const fileUploadIcon = <Icon name="file-upload" size={60} color="#cdcdcd" />;
  return (
    <View style={[baseContainer, { backgroundColor: "#3fbdd8" }]}>
      {fileUploadIcon}
    </View>
  );
};

export default UploadFile;
