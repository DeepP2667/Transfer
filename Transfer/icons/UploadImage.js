import { StyleSheet, View } from "react-native";
import Icon from "react-native-vector-icons/FontAwesome5";

const UploadImage = ({ baseContainer }) => {
  const imageIcon = <Icon name="file-image" size={60} color="#cdcdcd" />;
  return (
    <View style={[baseContainer, { backgroundColor: "#2f9688" }]}>
      {imageIcon}
    </View>
  );
};

export default UploadImage;
