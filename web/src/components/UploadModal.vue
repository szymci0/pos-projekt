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
import { FilesService } from '@/services/files';
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
		},
		uploadUrl: null,
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
		async handleUpload() {
			FilesService.uploadFile({
				file: this.uploadedFile,
				url: this.uploadUrl,
				onError: (res) => {
					return alert(res.detail);
				}
			})
			this.$emit('close')
		}
	}
}
</script>