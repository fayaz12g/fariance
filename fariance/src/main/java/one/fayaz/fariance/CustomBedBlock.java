package one.fayaz.fariance;

import net.minecraft.world.level.block.BedBlock;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.item.DyeColor;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

public class CustomBedBlock extends BedBlock {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);

    public static RegistryObject<BlockEntityType<CustomBedBlockEntity>> CUSTOM_BED_BLOCK_ENTITY;

    public CustomBedBlock(DyeColor color, BlockBehaviour.Properties properties) {
        super(color, properties);
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomBedBlockEntity(pos, state);
    }

    @Override
    public RenderShape getRenderShape(BlockState state) {
        return RenderShape.MODEL;
    }

    public static void registerBlockEntities() {
        CUSTOM_BED_BLOCK_ENTITY = BLOCK_ENTITIES.register(
                "custom_bed",
                () -> BlockEntityType.Builder.of(CustomBedBlockEntity::new,
                        ItemRegistry.GENERATED_BLOCKS.values().stream()
                                .filter(block -> block.get() instanceof CustomBedBlock)
                                .map(RegistryObject::get)
                                .toArray(CustomBedBlock[]::new)
                ).build(null)
        );

        BLOCK_ENTITIES.register(FMLJavaModLoadingContext.get().getModEventBus());
    }
}

class CustomBedBlockEntity extends BlockEntity {
    public CustomBedBlockEntity(BlockPos pos, BlockState state) {
        super(CustomBedBlock.CUSTOM_BED_BLOCK_ENTITY.get(), pos, state);
    }
}