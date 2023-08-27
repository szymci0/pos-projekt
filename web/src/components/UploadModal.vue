<template>
	<ModalComponent 
		:title="title"
		:show="show"
	>
		<template #body>
			<div class="d-flex justify-content-center">
				<input type="file" @change="handleSelect"/>
			</div>
		</template>
		<template #footer>
			<button @click="handleUpload">
				Upload
			</button>
		</template>
	</ModalComponent>
</template>
<script>
import ModalComponent from '@/components/ModalComponent';

export default {
	name: "UploadModal",
	components: { ModalComponent },
	props: {
		title: {
			type: String,
			default: "Upload file",
		},
		show: {
			type: Boolean,
			default: false,
		}
	},
	data() {
		return {
			uploadedFile: null,
		}
	},
	methods: {
		handleSelect(event) {
			this.uploadedFile = event.target.files[0];
		},
		handleUpload() {
			let uploadParams = new FormData();
			console.log(this.uploadedFile)
			uploadParams.append(
				'file',
				this.uploadedFile,
				this.uploadedFile.name,
			);
			console.log(uploadParams)
		}
	}
}
</script>